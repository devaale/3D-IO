import "./App.css";
import SettingGrid from "./components/Setting/SettingGrid";

import ConnectionState from "./components/Connection/ConnectionState";

import { SocketContext, socket } from "./context/socket";

const App = () => {
  return (
    <SocketContext.Provider value={socket}>
      <ConnectionState />
      <SettingGrid />
    </SocketContext.Provider>
  );
};

export default App;
