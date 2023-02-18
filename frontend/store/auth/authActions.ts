import axios from "axios";
import { createAsyncThunk } from "@reduxjs/toolkit";

const backend_url = process.env.DJANGO_API_BASE_URL

// export const RegisterUser = createAsyncThunk()