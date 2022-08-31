// third-party
import { configureStore } from '@reduxjs/toolkit';
import { setupListeners } from '@reduxjs/toolkit/query';

// project import
import menu from './reducers/menu';
import { apiSlice } from '../../src/api/apiSlice';
import authReducer from '../../src/pages/authentication/authSlice';
import { loadState, saveState } from 'localStorage';

// ==============================|| REDUX TOOLKIT - MAIN STORE ||============================== //
const persistedState = loadState();
const store = configureStore({
    reducer: {
        [apiSlice.reducerPath]: apiSlice.reducer,
        auth: authReducer,
        menu: menu
    },
    persistedState,
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(apiSlice.middleware),
    devTools: true
});
const { dispatch } = store;
store.subscribe(() => {
    saveState(store.getState());
});
setupListeners(store.dispatch);
export { store, dispatch };
