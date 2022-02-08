import { useContext } from "react";
import { SocketContext } from "../../context/socket";

const CountButton = () => {
  const socket = useContext(SocketContext);

  //   const handleClick = (e) => {
  //     e.preventDefault();
  //     if (!connection) return;

  //     socket.emit(events.PING_SERVER, { count: count });
  //     setCount(count + 1);
  //   };
  return (
    // <div>
    //   <p>Currently sent messages: {count}</p>
    //   <p>Currently received count value: {serverCount}</p>
    //   <button onClick={handleClick}>Click me!</button>
    // </div>
    <p>Hello ?</p>
  );
};
