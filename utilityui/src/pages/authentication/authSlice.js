import { createSlice } from '@reduxjs/toolkit';
import { loadState } from 'localStorage';

const persistedState = loadState();
const initialState = {
    user: '',
    token: '',
    business: '',
    refreshToken: ''
};
const authSlice = createSlice({
    name: 'auth',
    // initialState: { user: persistedState.auth.user, token: persistedState.auth.token, refreshToken: persistedState.auth.refreshToken },
    // initialState: { user: '', token: '', refreshToken: '' },
    initialState: { ...persistedState.auth },
    reducers: {
        setCredentials: (state, action) => {
            const { user, access, business, refresh } = action.payload;
            state.user = user;
            state.token = access;
            state.business = business;
            state.refreshToken = refresh;
        },
        logOut: (state, action) => {
            state.user = null;
            state.token = null;
        }
    }
});

export const { setCredentials, logOut } = authSlice.actions;

export default authSlice.reducer;

export const selectCurrentUser = (state) => state.auth.user;
export const selectCurrentBusiness = (state) => state.auth.business;
export const selectCurrentToken = (state) => state.auth.token;
