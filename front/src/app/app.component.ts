import {Component, OnInit} from '@angular/core';
import {HttpService} from '../services/http.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]
})
export class AppComponent implements OnInit {
  advertisements: any = [];
  pagesCount = 0;
  currentPage = 1;

  district = '';
  search = '';
  priceLower = 0;
  priceUpper = 1000000;
  roomsCount = '';

  constructor(private httpService: HttpService) {
  }

  ngOnInit() {
    this.refresh_list();
    this.currentPage = 1;
  }

  setPage(page: number) {
    this.currentPage = page;
    this.refresh_list();
  }

  filter() {
    this.refresh_list();
  }

  refresh_list() {
    this.httpService.getAdvertisements(this.currentPage, this.district, this.search, this.priceLower, this.priceUpper, this.roomsCount)
      .subscribe((data) => {
        console.log(data);
        this.advertisements = data.results;
        this.pagesCount = Math.ceil(data.count / 20.0);
      });
  }
}
