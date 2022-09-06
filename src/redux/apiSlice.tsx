import { createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { School, Raiting } from './types'


// Define a service using a base URL and expected endpoints
export const api = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({ baseUrl: 'https://virtserver.swaggerhub.com/80lvlapp/FirstLine/1.0.0/' }),
  
  endpoints: (builder) => ({
    getSchools: builder.query<School[], String>({
      query: () => `rest-schools`,
    }),
    getRaiting: builder.query<Raiting[], { id: string, startDate: string; endDate: string }>({
      query: (arg) => {
      const { id, startDate, endDate } = arg;
      return {
        url: 'rest-raiting/',
        params: { id, startDate, endDate }}}
      ,
    }),
  }),
})

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const { useGetSchoolsQuery, useGetRaitingQuery } = api