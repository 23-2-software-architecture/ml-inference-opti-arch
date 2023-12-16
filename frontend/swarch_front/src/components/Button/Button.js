import React, { useRef, useState } from "react";
import { useRecoilState } from "recoil";
import axios from "axios";
import { imageState, resultState } from "../../store";
import "./Button.scss";

function Button(props) {
	const [img, setImg] = useRecoilState(imageState);
	const [result, setResult] = useRecoilState(resultState);
	const [file, setFile] = useState(null);
	const imgRef = useRef();
	const formData = new FormData();
	const saveImgFile = (e) => {
		setFile(e.target.files[0]);

		const image = imgRef.current.files[0];
		const reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onloadend = () => {
			setImg({ img: reader.result, isEmpty: false });
		};
	};

	const url = "http://swarch.mhsong.cc/predict?model_name=" + props.model;
	const onImgUpload = async () => {
		formData.append("file", file);
		await axios
			.post(url, formData, {
				headers: {
					"Content-Type": "multipart/form-data",
					Accept: "multipart/form-data",
				},
			})
			.then((res) => {
				setResult(res.data.result);
			})
			.catch((e) => {
				setResult("Error");
			});
	};

	const onHomeClick = () => {
		window.location.replace("/");
	};

	if (img.isEmpty) {
		return (
			<form>
				<label id="buttonLabel" className="text" htmlFor="inputImage">
					{props.text}
				</label>
				<input
					style={{ display: "None" }}
					type="file"
					accept="image/*"
					id="inputImage"
					onChange={saveImgFile}
					ref={imgRef}
				/>
			</form>
		);
	} else if (!img.isEmpty && !result) {
		return (
			<button type="submit" className="text" onClick={onImgUpload}>
				Inference
			</button>
		);
	} else if (!img.isEmpty && result) {
		return (
			<button className="text" onClick={onHomeClick}>
				Home
			</button>
		);
	}
}
export default Button;
