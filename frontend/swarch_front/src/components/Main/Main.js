import React from "react";
import "./Main.css";
import InputBox from "../InputBox/InputBox";
import Title from "../Title/Title";
import Button from "../Button/Button";

function Main(props) {
  return (
    <div className="Main">
            <div className="Title"><Title/></div>
            <div className="InputBox"><InputBox/></div>
            <Button/>
    </div>
    )
};
export default Main;