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
    const [segmentation, setSegmentation] = React.useState("RANSAC");

    const handleClick = (e) => {
        setSegmentation(e.target.value);

        socket.emit(events.SET_ALGORITHM, { algorithm: e.target.value });
        console.log(e.target.value);
    };

    return (
        <FormControl fullWidth>
            <InputLabel id="segmentation-select-label">Segmentation</InputLabel>
            <Select
                labelId="segmentation-select-label"
                id="segmentation-label"
                value={segmentation}
                label="segmentation"
                onChange={handleClick}
            >
                <MenuItem value={"RANSAC"}>RANSAC</MenuItem>
                <MenuItem value={"PROSAC"}>PROSAC</MenuItem>
            </Select>
        </FormControl>
    );
};

export default ClusteringSelect;
