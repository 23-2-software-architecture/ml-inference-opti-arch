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
            <Button text="이미지 업로드"/>
    </div>
    )
};
export default Main;