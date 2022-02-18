import React from "react";
import socketio from "socket.io-client";

//TODO Add .env file
const SOCKET_URL = "http://127.0.0.1:5000";

export const socket = socketio.connect(SOCKET_URL);
export const SocketContext = React.createContext();
