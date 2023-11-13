import React, {useRef, useState} from "react";
import { useRecoilState } from "recoil";
import axios from "axios";
import { imageState, resultState } from "../../store";
import "./Button.scss";

function Button(props) {
  const [img ,setImg] = useRecoilState(imageState);
  const [result, setResult] = useRecoilState(resultState);
  const [file, setFile] = useState(null);
  const imgRef = useRef();
  const formData = new FormData();

  const saveImgFile = (e) => {
    setFile(e.target.files[0])

    const image = imgRef.current.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(image);
    reader.onloadend = () => {
      setImg({img:reader.result, isEmpty:false});
    };
  };

  // const test_url = "http://a6f463462c9034c92840c4e1cdadbd74-6b9510d16672c89b.elb.ap-northeast-2.amazonaws.com/predict?model_name=mobilenet_v1"
  const url = "http://swarch.mhsong.cc/predict?model_name=mobilenet_v1"
  const onImgUpload = async() => {
    formData.append("file", file)
    await axios.post(url, formData, {
      headers: {
        "Content-Type": "multipart/form-data", 
        "Accept":"multipart/form-data", 
        }
    }).then((res) => {
      console.log(res.data)
      setResult(res.data.result);
    }).catch((e) => {
      setResult("Error");
    });
  };

  const onHomeClick = () => {
    window.location.replace("/")
  }

  if(img.isEmpty) {
    return (
        <form>
          <label className="text" htmlFor="inputImage">{props.text}</label>
          <input 
            type="file"
            accept="image/*"
            id="inputImage"
            onChange={saveImgFile}
            ref={imgRef}
          />
        </form>
        )
  } else if (!img.isEmpty && !result) {
    return (
    <button type="submit" className="text" onClick={onImgUpload}>Inference</button>
    )
  } else if (!img.isEmpty && result) {
    return (<button className="text" onClick={onHomeClick}>Home</button>)
  }
};
export default Button;