import { createQueue } from 'kue';

const BLACKLISTED = ['4153518780', '4153518781'];

const sendNotification = (phoneNumber, message, job, done) => {
    job.progress(0, 100);

    if (BLACKLISTED.includes(phoneNumber)) {
	done(new Error(`Phone number ${phoneNumber} is blacklisted`));
	return
    }
    job.progress(50, 100);
    console.log(
	`Sending notification to ${phoneNumber},`,
	`with message: ${message}`);
    done()
};

const queue = createQueue();

queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
