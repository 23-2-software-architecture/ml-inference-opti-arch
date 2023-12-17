import React from "react";
import { useState } from "react";
import "./Main.css";
import InputBox from "../../components/InputBox/InputBox";
import Title from "../../components/Title/Title";
import Button from "../../components/Button/Button";
import RadioGroup from "../../components/RadioButton/RadioGroup";
import RadioButton from "../../components/RadioButton/RadioButton";

function Main(props) {
	const [value, setValue] = useState("mobilenet_v1");
	return (
		<div className="Main">
			<Title />
			<RadioGroup value={value} onChange={setValue}>
				<RadioButton value="mobilenet_v1" defaultChecked>
					MobileNetv1 (Image)
				</RadioButton>
				<RadioButton value="yolo_v5">YOLOv5 (Image)</RadioButton>
				<RadioButton value="bert_imdb">BERT (Text)</RadioButton>
			</RadioGroup>
			<InputBox state={value} />
			<Button text="File Upload" model={value} />
		</div>
	);
}
export default Main;
