import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';


@Injectable()
export class HttpService {
  prefix = 'https://lun-test-task.appspot.com/';

  constructor(private http: HttpClient) {
  }

  getAdvertisements(page = 1, itemsPerPage = 21, district = '', search = '', priceLower = '', priceUpper = '', roomsCount = '', sort = 'time__desc' ) {
    if (roomsCount === null) {
      roomsCount = '';
    }
    return this.http.get(this.prefix + 'search/ads/?district=' + district + '&info=' + search + '&limit=' + itemsPerPage + '&offset=' + ((page - 1) * itemsPerPage) + '&price__gt=' + priceLower + '&price__lt=' + priceUpper + '&rooms_count=' + roomsCount + '&sort=' + sort, {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    });
  }

  getStats() {
    return this.http.get(this.prefix + 'search/stats/', {
      headers: new HttpHeaders({
        'Content-Type':  'application/json'
      })
    });
  }
}
