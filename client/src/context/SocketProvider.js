// import React, { useState, useEffect } from "react";
// import socketio from "socket.io-client";

// //TODO Add .env file
// const SOCKET_URL = "http://127.0.0.1:5000";

// const SocketProvider = (props) => {
//   const [socketConn, setSocketConn] = useState(null);

//   useEffect(() => {
//     const socket = socketio.connect(SOCKET_URL);
//     setSocketConn(socket);
//     return () => socketio.disconnect(SOCKET_URL);
//   }, []);

//   return (
//     <SocketContext.Provider value={{ socket: socketConn }}>
//       {props.children}
//     </SocketContext.Provider>
//   );
// };
// export const SocketContext = React.createContext("socket");
// export default SocketProvider;
