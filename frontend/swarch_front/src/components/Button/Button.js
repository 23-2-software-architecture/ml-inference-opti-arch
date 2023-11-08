import React from "react";
import "./Button.scss";

function Button(props) {
  return (
    // TODO: props로 페이지마다 text 변경
        <button className="text">{props.text}</button>
    )
};
export default Button;