import "./App.css";
import React, { useEffect, useState } from "react";
import socket from "./sockets";

const App = () => {
  const [count, setCount] = useState(0)
  const [serverCount, setServerCount] = useState(0)
  const [connection, setConnection] = useState(false);

  useEffect(() => {
    socket.on('connect', () => {
      setConnection(true)
    });

    socket.on('disconnect', () => {
      setConnection(false)
      setCount(0)
      setServerCount(0)
    });

    socket.on('message', (data) => {
      setServerCount(data.count)
    })
  });

  const handleClick = (e) => {
    if (!connection) return;

    e.preventDefault();
    socket.emit('message', {'count': count});
    setCount(count + 1)
  }
  return (<div className="App">
    <p>
      It's {connection ? 'Connected' : 'Disconnected'}
    </p>
    <p>
      Currently sent messages: {count}
    </p>
    <p>
      Currently received count value: {serverCount}
    </p>
    <button onClick={handleClick}>Click me!</button>
  </div>);
};

export default App;
