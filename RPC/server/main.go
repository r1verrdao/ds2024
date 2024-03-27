// File Sever: sever/main.go
package main

import (
	"log"
	"net"
	"net/rpc"
)

type GreetingService struct{}

func (p *GreetingService) Hello(request string, reply *string) error {
	*reply = "Hello " + request

	return nil
}

func main() {
	
	// Register a service with name 'Greeting' and GreetingService typpe
	rpc.RegisterName("Greeting", new(GreetingService))

	// Create a TCP server on port 1234
	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal("Can not create sever because:", err)
	}
    
    log.Print("Sever is listening on port 1234")

	for {
		// Accept connection
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Accept error:", err)
		}


		// Serve the call of Client on another goroutine for continue receiving other RPCs
		go rpc.ServeConn(conn)
	}
}


