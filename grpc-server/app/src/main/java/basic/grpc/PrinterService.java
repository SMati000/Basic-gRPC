package basic.grpc;

import basic.grpc.printer.PrinterGrpc;
import basic.grpc.printer.ProtobufTest.Mensaje;
import io.grpc.stub.StreamObserver;
import java.io.IOException;
import java.net.InetAddress;
import java.util.Random;

public final class PrinterService extends PrinterGrpc.PrinterImplBase {
	private final String serverName;

	public PrinterService(String serverName) {
		if (serverName == null) {
			serverName = determineHostname();
		}
		this.serverName = serverName;
	}
	@Override
	public void printThis(Mensaje req, StreamObserver<Mensaje> res) {
		Mensaje mensaje = Mensaje.newBuilder().setPrintThis("I am responding back: " + req.getPrintThis()).build();
		res.onNext(mensaje);
		res.onCompleted();
	}

	private static String determineHostname() {
		try {
			return InetAddress.getLocalHost().getHostName();
		} catch (IOException ex) {}

		return "generated-" + new Random().nextInt();
	}
}
