import { useContext, useState } from "react";
import { SocketContext } from "../../context/socket";
import events from "../../constants/events";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import React from 'react';
import Select from '@mui/material/Select';

const ClusteringSelect = () => {
    const socket = useContext(SocketContext);
    const [clustering, setClustering] = React.useState("DBSCAN");

    const handleClick = (e) => {
        setClustering(e.target.value);

        socket.emit(events.SET_ALGORITHM, { algorithm: e.target.value });
        console.log(e.target.value);
    };

    return (
        <FormControl fullWidth>
            <InputLabel id="clustering-select-label">Clustering</InputLabel>
            <Select
                labelId="clustering-select-label"
                defaultValue={30}
                id="clustering-label"
                value={clustering}
                label="Clustering"
                onChange={handleClick}
            >
                <MenuItem value={"DBSCAN"}>DBSCAN</MenuItem>
                <MenuItem value={"K-MEANS"}>K-MEANS</MenuItem>
                <MenuItem value={"HDBSCAN"}>HDBSCAN</MenuItem>
            </Select>
        </FormControl>
    );
};

export default ClusteringSelect;
