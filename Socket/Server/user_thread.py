def user_handle(client):
    # Customize an exception
    class Exit_Exception(Exception):
        pass
    # set recv unblock
    client.setblocking(0)
    print(client)
    while True:
        try:
            cmd = client.recv(512).decode()
            if cmd == "SayHi":
                client.send("Hello,I'm iron man!".encode())
            elif cmd == "q" or data == "quit":
                client.send("GoodBye".encode())
                raise Exit_Exception
        except Exit_Exception:
            print("Bye")
            client.close()
            socks.remove(client)
            sys.exit(1)
        except Exception:
                time.sleep(1)
                pass
