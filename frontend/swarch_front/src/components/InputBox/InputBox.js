import React from "react";
import "./InputBox.css";
import { useRecoilValue } from "recoil";
import { imageState, resultState, textState } from "../../store";

function InputBox({ state }) {
	const imgFile = useRecoilValue(imageState);
	const result = useRecoilValue(resultState);
	const text = useRecoilValue(textState);

	if (!result && text.isEmpty) {
		return (
			<div className="InputBox">
				{imgFile.isEmpty ? <p>파일을 업로드 해주세요.</p> : <img src={imgFile.img} alt="text" />}
			</div>
		);
	}
	if (state === "mobilenet_v1") {
		var result_probability = result.result_probability * 100;
		result_probability = Math.round(result_probability * 1000) / 1000;
		return (
			<div className="InputBox">
				{result.result_class} 인 것 같습니다!
				<br></br>
				{result_probability} % 정확도
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
