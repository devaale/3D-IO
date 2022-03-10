import Grid from "@mui/material/Grid";
import { Container } from "@mui/material";

import SettingItem from "./SettingItem";

import { useEffect, useState } from "react";

const SettingGrid = () => {
  const [settingsData, setSettingsData] = useState([]);

  useEffect((e) => {
    fetchData();
  }, []);

  const fetchData = () => {
    fetch(`http://localhost:8000/settings`)
      .then((response) => response.json())
      .then((data) => {
        setSettingsData(data);
      })
      .catch((err) => {
        setSettingsData(null);
      });
  };

  return (
    <Container maxWidth="md">
      <Grid container spacing={2} marginTop={10}>
        {settingsData &&
          settingsData.map((setting) => (
            <SettingItem key={setting.id} setting={setting} />
          ))}
      </Grid>
    </Container>
  );
};

export default SettingGrid;
