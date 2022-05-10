import Grid from "@mui/material/Grid";
import Slider from "@mui/material/Slider";
import Typography from "@mui/material/Typography";
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import React, { Component } from 'react';
import { useContext, useState } from "react";

import events from "../../constants/events";
import { SocketContext } from "../../context/socket";

const SettingItem = ({ setting }) => {
  const socket = useContext(SocketContext);
  const [value, setValue] = useState(setting.value);

  const handleSliderChange = (event, newValue) => {
    if (value === newValue) return;
    setValue(newValue);
    sendSettingUpdate(setting.id, newValue);
  };

  const sendSettingUpdate = (id, newValue) => {
    socket.emit(events.UPDATE_SETTING, { id: id, value: newValue });
  };



  return (
    <Grid key={setting.id} item xs={12} md={6}>
      <Card sx={{ display: 'flex' }}>
        <CardContent sx={{ flex: '1 0 auto' }}>
          <Typography mb={5}>{setting.description}</Typography>
          <Slider
            value={value}
            onChange={handleSliderChange}
            valueLabelDisplay="on"
            step={setting.step}
            min={setting.min_value}
            max={setting.max_value}
          />
        </CardContent>
      </Card>
    </Grid >
  );
};

export default SettingItem;
