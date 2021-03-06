import "./ConnectionState.css";
import { useContext, useState, useEffect } from "react";
import { SocketContext } from "../../context/socket";
import ConnectionButton from "./ConnectionButton";
import events from "../../constants/events";
import React, { Component } from 'react';
const ConnectionState = () => {
  const socket = useContext(SocketContext);
  const [connected, setConnected] = useState(false);
  const [data, setData] = useState([]);

  useEffect((e) => {
    mountEventListeners();

    return () => {
      unmountEventListeners();
    };
  });

  const handleConnect = () => {
    setConnected(true);
    console.log("Connected");
    //Maybe some other functions calls down here
  };

  const handleDisconnect = () => {
    setConnected(false);
    console.log("Disconnected");
    //Maybe some other functions calls down here
  };

  const mountEventListeners = () => {
    socket.on(events.CONNECT, handleConnect);
    socket.on(events.DISCONNECT, handleDisconnect);
  };

  const unmountEventListeners = () => {
    socket.off(events.CONNECT, handleConnect);
    socket.off(events.DISCONNECT, handleDisconnect);
  };

  return (
    <div className="ConnectionState">
      <p>It's {connected ? "Connected" : "Disconnected"}</p>
    </div>
  );
};

export default ConnectionState;
