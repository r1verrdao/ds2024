// File Client: client/main.go
package main

import (
	"fmt"
	"log"
	"net/rpc"
)

func main() {

	// Create a client connecting to 'localhost:1234'
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal(err)
	}

	var reply string
	
	// Call RPC with 'Greeting' service and 'Hello' method
	err = client.Call("Greeting.Hello", "Riverr", &reply)
	if err != nil {
		log.Fatal(err)
	}


	fmt.Println(reply)
}


