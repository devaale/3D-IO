import Grid from "@mui/material/Grid";
import Slider from "@mui/material/Slider";
import Typography from "@mui/material/Typography";

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
      <Typography gutterBottom>{setting.description}</Typography>
      <Slider
        value={value}
        onChange={handleSliderChange}
        valueLabelDisplay="auto"
        step={setting.step}
        marks
        min={setting.min_value}
        max={setting.max_value}
      />
    </Grid>
  );
};

export default SettingItem;
