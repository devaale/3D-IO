import "./App.css";
import ConnectionState from "./components/Connection/ConnectionState";
import { SocketContext, socket } from "./context/socket";

const App = () => {
  return (
    <SocketContext.Provider value={socket}>
      <ConnectionState />
    </SocketContext.Provider>
  );
};

export default App;
