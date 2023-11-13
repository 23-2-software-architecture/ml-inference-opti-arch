import React from "react";
import "./Main.css";
import InputBox from "../../components/InputBox/InputBox";
import Title from "../../components/Title/Title";
import Button from "../../components/Button/Button";

function Main(props) {
    return (
    <div className="Main">
            <Title/>
            <InputBox/>
            <Button text="Image Upload"/>
    </div>
    )
};
export default Main;