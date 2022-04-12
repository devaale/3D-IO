import "./App.css";
import SettingGrid from "./components/Setting/SettingGrid";

import ConnectionState from "./components/Connection/ConnectionState";

import { SocketContext, socket } from "./context/socket";
import { QueryClientProvider, QueryClient } from "react-query";
import TriggerButton from "./components/Buttons/TriggerButton";

const queryClient = new QueryClient();

const App = () => {
  return (
    <QueryClientProvider client={queryClient}>
      <SocketContext.Provider value={socket}>
        <ConnectionState />
        <TriggerButton />
        <SettingGrid />
      </SocketContext.Provider>
    </QueryClientProvider>
  );
};

export default App;
