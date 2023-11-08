import { atom } from 'recoil';

const imageState = atom({
  key: 'imageState',
  default: {
    img: '',
    isEmpty: true
  },
});

export default imageState;