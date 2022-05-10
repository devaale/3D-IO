import { useContext, useState } from "react";
import { SocketContext } from "../../context/socket";
import events from "../../constants/events";
import Button from "@mui/material/Button";
import React, { Component } from 'react';
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
      <Button variant="contained" onClick={handleClick}>
        Click Me !
      </Button>
    </div>
  );
};

export default CountButton;
