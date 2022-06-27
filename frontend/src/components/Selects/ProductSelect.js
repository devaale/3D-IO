import { useContext, useState } from "react";
import { SocketContext } from "../../context/socket";
import events from "../../constants/events";
import InputLabel from '@mui/material/InputLabel';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import React from 'react';
import Select from '@mui/material/Select';

const ProductSelect = () => {
    const socket = useContext(SocketContext);
    const [product, setProduct] = React.useState("PRODUCT_TYPE_ONE");

    const handleClick = (e) => {
        setProduct(e.target.value);

        socket.emit(events.SET_PRODUCT, {});
        console.log(e.target.value);
    };

    return (
        <FormControl fullWidth>
            <InputLabel id="product-select-label">Product</InputLabel>
            <Select
                labelId="product-select-label"
                defaultValue={30}
                id="product-label"
                value={product}
                label="Product"
                onChange={handleClick}
            >
                <MenuItem value={"PRODUCT_TYPE_ONE"}>PRODUCT_TYPE_ONE</MenuItem>
                <MenuItem value={"PRODUCT_TYPE_TWO"}>PRODUCT_TYPE_TWO</MenuItem>
                <MenuItem value={"PRODUCT_TYPE_THREE"}>PRODUCT_TYPE_THREE</MenuItem>
            </Select>
        </FormControl>
    );
};

export default ProductSelect;
