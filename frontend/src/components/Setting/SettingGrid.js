import Grid from "@mui/material/Grid";
import { Container } from "@mui/material";

import SettingItem from "./SettingItem";
import React, { Component } from 'react';
import { useQuery } from "react-query";

const SettingGrid = () => {
  // Functions
  async function getSettings() {
    const res = await fetch(`http://localhost:8000/settings`);
    return res.json();
  }

  //Queries
  const { isLoading, isError, data, error } = useQuery("settings", getSettings);

  //Reponse
  if (isLoading) {
    return <span>Loading...</span>;
  }

  if (isError) {
    return <span>Error: {error.message}</span>;
  }

  return (
    <Container maxWidth="lg">
      <Grid container spacing={2} marginTop={0}>
        {data &&
          data.map((setting) => (
            <SettingItem key={setting.id} setting={setting} />
          ))}
      </Grid>
    </Container>
  );
};

export default SettingGrid;
