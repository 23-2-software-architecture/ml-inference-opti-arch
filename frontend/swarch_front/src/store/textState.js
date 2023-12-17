import { atom } from "recoil";

const textState = atom({
	key: "textState",
	default: {
		text: "",
		isEmpty: true,
	},
});

export default textState;
