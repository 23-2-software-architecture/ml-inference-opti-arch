import React from "react";
import './InputBox.css'
import { useRecoilValue } from "recoil";
import { imageState, resultState } from "../../store";

function InputBox(props) {
  const imgFile = useRecoilValue(imageState);
  const result = useRecoilValue(resultState);

  if(!result){
    return (
        <div className="InputBox">
          {
            imgFile.isEmpty ?
            <p>이미지를 업로드 해주세요.</p> :
            <img src={imgFile.img} alt="img"/>
          }
        </div>
      )
  }
  return (
        <div className="InputBox">
          {result}
        </div>
    )
};
export default InputBox;