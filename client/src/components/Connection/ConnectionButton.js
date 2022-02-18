import { useContext, useState } from "react";
import { SocketContext } from "../../context/socket";
import events from "../../constants/events";

const CountButton = (props) => {
  const socket = useContext(SocketContext);
  const [count, setCount] = useState(0);

  const handleClick = (e) => {
    e.preventDefault();
    if (!props.connected) return;

    socket.emit(events.PING_SERVER, { count: count });
    setCount(count + 1);
  };

  return (
    <div>
      <p>Currently sent messages: {count}</p>
      <button onClick={handleClick}>Click me!</button>
    </div>
  );
};

export default CountButton;
