import {Component, OnInit} from '@angular/core';
import {HttpService} from '../services/http.service';
import {ActivatedRoute, Params, Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [HttpService]
})
export class AppComponent implements OnInit {
  advertisements: any = [];
  itemsPerPage = 21;
  pagesCount = 0;
  currentPage = 1;

  district = '';
  search = '';
  priceLower = 0;
  priceUpper = 1000000;
  roomsCount = '';
  sort = 'time__desc';

  stats: any = {
    price: {
      min: 0,
      max: 1000000
    },
    rooms_count: {
      max: 10
    }
  };

  constructor(private httpService: HttpService, private activateRoute: ActivatedRoute, private router: Router) {
  }

  ngOnInit() {
    this.httpService.getStats()
      .subscribe((data) => {
        this.stats = data;
        console.log(this.stats);
        this.priceLower = this.stats.price.min;
        this.priceUpper = this.stats.price.max;
        this.activateRoute.queryParams
          .subscribe(params => {
            console.log(params);
            if (params.page) {
              this.currentPage = Number(params.page);
              this.sort = params.sort;
              this.district = params.district;
              this.search = params.search;
              this.priceLower = params.priceLower;
              this.priceUpper = params.priceUpper;
              this.roomsCount = params.roomsCount;
              this.refresh_list();
            }
          });
      });
    this.refresh_list();
  }

  setPage(page: number) {
    this.currentPage = page;
    this.refresh_list();
  }

  filter() {
    // this.refresh_list();
    this.router.navigate([''], {
      queryParams: {
        page: 1,
        district: this.district,
        search: this.search,
        priceLower: this.priceLower,
        priceUpper: this.priceUpper,
        roomsCount: this.roomsCount,
        sort: this.sort,
      }
    });
  }

  refresh_list() {
    this.httpService.getAdvertisements(this.currentPage, this.itemsPerPage, this.district, this.search, this.priceLower.toString(10), this.priceUpper.toString(10), this.roomsCount, this.sort)
      .subscribe((data) => {
        // @ts-ignore
        this.advertisements = data.results;
        // @ts-ignore
        this.pagesCount = Math.ceil(data.count / this.itemsPerPage);
      });
  }
}
