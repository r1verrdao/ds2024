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
	// Đăng ký service với tên là Greeting có kiểu là GreetingService
	rpc.RegisterName("Greeting", new(GreetingService))

	// Tạo sever chạy trên port 1234
	listener, err := net.Listen("tcp", ":1234")
	if err != nil {
		log.Fatal("Can not create sever because:", err)
	}
    
    log.Print("Sever is listening on port 1234")

	for {
		// Chấp nhận connection
		conn, err := listener.Accept()
		if err != nil {
			log.Fatal("Accept error:", err)
		}

		// Phục vụ lời gọi Client trên một goroutine khác để tiếp tục nhận các lời gọi RPC khác
		go rpc.ServeConn(conn)
	}
}


