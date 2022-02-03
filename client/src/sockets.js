import socketIO from "socket.io-client";

const ADDRESS = 'http://127.0.0.1:5000';

const socket = socketIO(ADDRESS);

export default socket;
