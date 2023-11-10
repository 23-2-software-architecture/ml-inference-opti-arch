import React, {useRef} from "react";
import { redirect } from "react-router-dom";
import "./Button.scss";
import { useRecoilState } from "recoil";
import { imageState } from "../../store";

function Button(props) {
  const [img ,imgSave] = useRecoilState(imageState);
  const imgRef = useRef();

  const saveImgFile = () => {
    const file = imgRef.current.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onloadend = () => {
      imgSave({img:reader.result, isEmpty:false});
    };
  };

  const onImgUpload = async (event) => {
    // setLogoLoading(true)
    const formData = new FormData();
    formData.append("img", img.img);
    // const response = await api.post('/api_address', formData)
    // setLogoLoading(false)
  };

  const handleClick = () => {
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
      }
    return (
      // 이미지 백엔드로 전송
      // 결과 페이지로 이동
        <button className="text" onClick={handleClick}>Inference</button>
      )
};
export default Button;