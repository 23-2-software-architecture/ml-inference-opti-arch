import "./RadioButton.css";
import { useContext } from "react";
import ButtonContext from "./ButtonContext";
function RadioButton({ children, value, name, defaultChecked, disabled }) {
	const group = useContext(ButtonContext);

	return (
		<label>
			<input
				type="radio"
				value={value}
				name={name}
				disabled={disabled || group.disabled}
				checked={group.value !== undefined ? value === group.value : undefined}
				onChange={(e) => group.onChange && group.onChange(e.target.value)}
			/>
			{children}
		</label>
	);
}
export default RadioButton;
