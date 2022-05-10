import { useContext, useState } from "react";
import { SocketContext } from "../../context/socket";
import events from "../../constants/events";
import Button from "@mui/material/Button";
import React, { Component } from 'react';
const CameraButton = () => {
    const socket = useContext(SocketContext);
    const [count, setCount] = useState(0);

    const handleClick = (e) => {
        e.preventDefault();

        socket.emit(events.CAMERA_START, {});
        setCount(count + 1);
    };

    return (
        <div>
            <Button variant="outlined" color="success" onClick={handleClick}>
                START
            </Button>
        </div>
    );
};

export default CameraButton;
