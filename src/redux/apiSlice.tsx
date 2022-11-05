import { createApi, fetchBaseQuery} from '@reduxjs/toolkit/query/react';
import { createSlice, PayloadAction } from '@reduxjs/toolkit';
import { School, Rating, RatingSportsman, RatingTournament } from './types'


// Define a service using a base URL and expected endpoints
export const api = createApi({
  reducerPath: 'api',
  //baseQuery: fetchBaseQuery({ baseUrl: 'https://virtserver.swaggerhub.com/80lvlapp/FirstLine/1.0.0/' }),
  baseQuery: fetchBaseQuery({ baseUrl: 'http://sportsrating.ru:8080/fist-line/api/v1/' }),
  
  endpoints: (builder) => ({
    getSchools: builder.query<School[], String>({
      //query: () => `rest-schools`,
      query: () => `schools`
    }),
    getRating: builder.query<Rating[], { id: string, startDate: string; endDate: string }>({
      query: (arg) => {
      const { id, startDate, endDate } = arg;
      return {
        url: 'rest-rating/',
        params: { id, startDate, endDate }}}
      ,
    }),
    getRatingSportsman: builder.query<RatingSportsman, { id: string, startDate: string; endDate: string }>({
      query: (arg) => {
      const { id, startDate, endDate } = arg;
      return {
        url: 'rest-rating-sportsman/',
        params: { id, startDate, endDate }}}
      ,
    }),
    getRatingTournament: builder.query<RatingTournament, { id: string, idTournament : string }>({
      query: (arg) => {
      const { id, idTournament } = arg;
      return {
        url: 'rest-rating-tournament/',
        params: { id, idTournament }}}
      ,
    }),
  }),
})

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const { useGetSchoolsQuery, useGetRatingQuery, useGetRatingSportsmanQuery, useGetRatingTournamentQuery } = api