import "./App.css";
import Box from '@mui/material/Box';
import SettingGrid from "./components/Setting/SettingGrid";
import React from 'react';
import { useContext } from "react";
import { SocketContext, socket } from "./context/socket";
import events from "./constants/events";
import Grid from '@mui/material/Grid';
import { QueryClientProvider, QueryClient } from "react-query";
import TriggerButton from "./components/Buttons/TriggerButton";
import CameraButton from "./components/Buttons/CameraButton";
import { Container } from "@mui/material";
import ProductSelect from "./components/Selects/ProductSelect";
import ClusteringSelect from "./components/Selects/ClusteringSelect";
import SegmentationSelect from "./components/Selects/SegmentationSelect";
import DetectButton from "./components/Buttons/DetectButton";
import TrainButton from "./components/Buttons/TrainButton";

const queryClient = new QueryClient();

const App = () => {

  return (
    <QueryClientProvider client={queryClient}>
      <SocketContext.Provider value={socket}>
        <Container maxWidth="lg">

          <Grid container spacing={2} marginTop={2}>
            <Grid item xs={3} marginLeft={0}>
              <CameraButton />
            </Grid>
            <Grid item xs={3}>
              <TriggerButton />
            </Grid>
            <Grid item xs={3}>
              <DetectButton />
            </Grid>
            <Grid item xs={3}>
              <TrainButton />
            </Grid>
          </Grid>
          <Grid container spacing={2} marginTop={2}>
            <Grid item xs={3} marginLeft={20}>
              <Box sx={{ minWidth: 80 }}>
                <ProductSelect />
              </Box>
            </Grid>
            <Grid item xs={3}>
              <Box sx={{ minWidth: 80 }}>
                <ClusteringSelect />
              </Box>
            </Grid>
            <Grid item xs={3}>
              <Box sx={{ minWidth: 80 }}>
                <SegmentationSelect />
              </Box>
            </Grid>
          </Grid>
          <SettingGrid />
        </Container>
      </SocketContext.Provider>
    </QueryClientProvider >
  );
};

export default App;
