export const loadState = () => {
    try {
        const serializedState = localStorage.getItem('state');
        if (serializedState === null) {
            return '';
        }
        return JSON.parse(serializedState);
    } catch (err) {
        return '';
    }
};
export const saveState = (state) => {
    try {
        const serializesState = JSON.stringify(state);
        localStorage.setItem('state', serializesState);
    } catch (err) {
        console.log(err);
    }
};
