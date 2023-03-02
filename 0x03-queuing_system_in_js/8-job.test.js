import kue from 'kue';
import mocha from 'mocha';
import sinon from 'sinon';
import {expect, assert } from 'chai';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

describe('createPushNotificationsJobs', function(){
  it('display a error message if jobs is not an array', function(){
    const jobs = 1;
    expect(createPushNotificationsJobs.bind(jobs, queue)).to.equal(new Error('Job is not an array'));
  });

  it('create two new jobs to the queue', function(){
    const consoleSpy = sinon.spy(console, 'log');
    const jobs = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account'
      },
      {
        phoneNumber: '4153378780',
        message: 'This is the code 2345 to verify your account'
      }
    ];
    createPushNotificationsJobs(jobs, queue);
	  
    expect(consoleSpy.calledWith('Notification job created:')).to.be.true;
    expect(consoleSpy.calledWith('Notification job created:')).to.be.true;
  });
})

