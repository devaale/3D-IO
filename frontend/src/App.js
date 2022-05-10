import "./App.css";
import Box from '@mui/material/Box';
import SettingGrid from "./components/Setting/SettingGrid";
import React, { Component } from 'react';
import ConnectionState from "./components/Connection/ConnectionState";
import Grid from '@mui/material/Grid';
import { SocketContext, socket } from "./context/socket";
import { QueryClientProvider, QueryClient } from "react-query";
import TriggerButton from "./components/Buttons/TriggerButton";
import CameraButton from "./components/Buttons/CameraButton";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import Select from '@mui/material/Select';
import { Container } from "@mui/material";
const queryClient = new QueryClient();

const App = () => {
  const [age, setAge] = React.useState('');
  const [cls, setCls] = React.useState('');
  const [sgm, setSgm] = React.useState('');

  const handleChange = (event) => {
    setAge(event.target.value);
  };

  const handleChangeClustering = (event) => {
    setCls(event.target.value);
  };

  const handleChangeSegmentation = (event) => {
    setSgm(event.target.value);
  };

  return (
    <QueryClientProvider client={queryClient}>
      <SocketContext.Provider value={socket}>
        <Container maxWidth="lg">

          <Grid container spacing={2} marginTop={2}>
            <Grid item xs={4} marginLeft={44}>
              <CameraButton />
            </Grid>
            <Grid item xs={4}>
              <TriggerButton />
            </Grid>
          </Grid>
          <Grid container spacing={2} marginTop={2}>
            <Grid item xs={3} marginLeft={20}>
              <Box sx={{ minWidth: 80 }}>
                <FormControl fullWidth>
                  <InputLabel id="demo-simple-select-label">Product</InputLabel>
                  <Select
                    labelId="demo-simple-select-label"
                    id="demo-simple-select"
                    label="Product"
                    onChange={handleChange}
                  >
                    <MenuItem value={10}>Product_TEST</MenuItem>
                  </Select>
                </FormControl>
              </Box>
            </Grid>
            <Grid item xs={3}>
              <Box sx={{ minWidth: 80 }}>
                <FormControl fullWidth>
                  <InputLabel id="demo-simple-select-label-c">Clustering</InputLabel>
                  <Select
                    labelId="demo-simple-select-label-c"
                    id="demo-simple-select-c"
                    value="DBSCAN"
                    label="Clustering"
                    onChange={handleChangeClustering}
                  >
                    <MenuItem value={10}>DBSCAN</MenuItem>
                  </Select>
                </FormControl>
              </Box>
            </Grid>
            <Grid item xs={3}>
              <Box sx={{ minWidth: 80 }}>
                <FormControl fullWidth>
                  <InputLabel id="demo-simple-select-label-s">Segmentation</InputLabel>
                  <Select
                    labelId="demo-simple-select-label-s"
                    id="demo-simple-select-s"
                    value="RANSAC"
                    label="Segmentation"
                    onChange={handleChangeSegmentation}
                  >
                    <MenuItem value={10}>RANSAC</MenuItem>
                  </Select>
                </FormControl>
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
