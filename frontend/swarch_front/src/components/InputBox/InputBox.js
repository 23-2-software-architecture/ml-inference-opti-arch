import React from "react";
import "./InputBox.css";
import { useRecoilValue } from "recoil";
import { imageState, resultState } from "../../store";

function InputBox({ state }) {
	const imgFile = useRecoilValue(imageState);
	const result = useRecoilValue(resultState);

	if (!result) {
		return (
			<div className="InputBox">
				{imgFile.isEmpty ? <p>파일을 업로드 해주세요.</p> : <img src={imgFile.img} alt="img" />}
			</div>
		);
	}
	if (state === "mobilenet_v1") {
		return (
			<div className="InputBox">
				{result.result_class}
				<br></br>
				{result.result_probability}
			</div>
		);
	} else if (state === "yolo_v5") {
		return (
			<div className="InputBox">
				<img src={`data:image/png;base64,${result.result}`} alt="yolo" />
				<br></br>
			</div>
		);
	} else if (state === "bert_imdb") {
		return (
			<div className="InputBox">
				{result.result}
				<br></br>
			</div>
		);
	}
}
export default InputBox;
