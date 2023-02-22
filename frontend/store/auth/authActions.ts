import axios from "axios";
import { createAsyncThunk } from "@reduxjs/toolkit";

const DJANGO_API: string = process.env.NEXT_PUBLIC_DJANGO_API_BASE_URL!
