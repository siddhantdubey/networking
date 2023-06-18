open Unix

let socket_server () =
  let sock = socket PF_INET SOCK_DGRAM 0 in
  let server_address = ADDR_INET (inet_addr_any, 12345) in 
  bind sock server_address;
  let buffer = Bytes.create 1024 in 
  while true do
    let n, sender_address = recvfrom sock buffer 0 1024 [] in 
    let received_message = Bytes.sub_string buffer 0 n in
    let reply = String.uppercase_ascii received_message in
    let _ = sendto sock (Bytes.of_string reply) 0 (String.length reply) [] sender_address in
    ()
  done

let _ = socket_server ()
